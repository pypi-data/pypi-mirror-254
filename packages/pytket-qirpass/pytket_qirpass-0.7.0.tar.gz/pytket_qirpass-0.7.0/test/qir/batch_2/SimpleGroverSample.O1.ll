; ModuleID = '.\qir\SimpleGroverSample.ll'
source_filename = ".\\qir\\SimpleGroverSample.ll"
target datalayout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-windows-msvc19.29.30040"

%Qubit = type opaque
%Array = type opaque
%Result = type opaque
%String = type opaque

@0 = internal constant [3 x i8] c"()\00"

define internal fastcc void @Microsoft__Quantum__Samples__SimpleGrover__CCX__body(%Qubit* %control1, %Qubit* %control2, %Qubit* %target) unnamed_addr {
entry:
  call fastcc void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %target)
  call fastcc void @Microsoft__Quantum__Intrinsic__T__adj(%Qubit* %control1)
  call fastcc void @Microsoft__Quantum__Intrinsic__T__adj(%Qubit* %control2)
  call fastcc void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %target, %Qubit* %control1)
  call fastcc void @Microsoft__Quantum__Intrinsic__T__body(%Qubit* %control1)
  call fastcc void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %control2, %Qubit* %target)
  call fastcc void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %control2, %Qubit* %control1)
  call fastcc void @Microsoft__Quantum__Intrinsic__T__body(%Qubit* %target)
  call fastcc void @Microsoft__Quantum__Intrinsic__T__adj(%Qubit* %control1)
  call fastcc void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %control2, %Qubit* %target)
  call fastcc void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %target, %Qubit* %control1)
  call fastcc void @Microsoft__Quantum__Intrinsic__T__adj(%Qubit* %target)
  call fastcc void @Microsoft__Quantum__Intrinsic__T__body(%Qubit* %control1)
  call fastcc void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %control2, %Qubit* %control1)
  call fastcc void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %target)
  ret void
}

define internal fastcc void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %qubit) unnamed_addr {
entry:
  call void @__quantum__qis__h__body(%Qubit* %qubit)
  ret void
}

define internal fastcc void @Microsoft__Quantum__Intrinsic__T__adj(%Qubit* %qubit) unnamed_addr {
entry:
  call void @__quantum__qis__t__adj(%Qubit* %qubit)
  ret void
}

define internal fastcc void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %control, %Qubit* %target) unnamed_addr {
entry:
  call void @__quantum__qis__cnot__body(%Qubit* %control, %Qubit* %target)
  ret void
}

define internal fastcc void @Microsoft__Quantum__Intrinsic__T__body(%Qubit* %qubit) unnamed_addr {
entry:
  call void @__quantum__qis__t__body(%Qubit* %qubit)
  ret void
}

define internal fastcc void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %qubit) unnamed_addr {
entry:
  call fastcc void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %qubit)
  ret void
}

define internal fastcc void @Microsoft__Quantum__Samples__SimpleGrover__SearchForMarkedInput__body() unnamed_addr {
entry:
  %qubits = call %Array* @__quantum__rt__qubit_allocate_array(i64 2)
  call void @__quantum__rt__array_update_alias_count(%Array* %qubits, i32 1)
  %0 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 0)
  %1 = bitcast i8* %0 to %Qubit**
  %2 = load %Qubit*, %Qubit** %1, align 8
  call fastcc void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %2)
  %3 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 1)
  %4 = bitcast i8* %3 to %Qubit**
  %5 = load %Qubit*, %Qubit** %4, align 8
  call fastcc void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %5)
  %outputQubit = call %Qubit* @__quantum__rt__qubit_allocate()
  call fastcc void @Microsoft__Quantum__Intrinsic__X__body(%Qubit* %outputQubit)
  call fastcc void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %outputQubit)
  %6 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 0)
  %7 = bitcast i8* %6 to %Qubit**
  %8 = load %Qubit*, %Qubit** %7, align 8
  call fastcc void @Microsoft__Quantum__Intrinsic__X__body(%Qubit* %8)
  %9 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 0)
  %10 = bitcast i8* %9 to %Qubit**
  %11 = load %Qubit*, %Qubit** %10, align 8
  %12 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 1)
  %13 = bitcast i8* %12 to %Qubit**
  %14 = load %Qubit*, %Qubit** %13, align 8
  call fastcc void @Microsoft__Quantum__Samples__SimpleGrover__CCX__body(%Qubit* %11, %Qubit* %14, %Qubit* %outputQubit)
  %15 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 0)
  %16 = bitcast i8* %15 to %Qubit**
  %17 = load %Qubit*, %Qubit** %16, align 8
  call fastcc void @Microsoft__Quantum__Intrinsic__X__adj(%Qubit* %17)
  call fastcc void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %outputQubit)
  call fastcc void @Microsoft__Quantum__Intrinsic__X__adj(%Qubit* %outputQubit)
  call void @__quantum__rt__qubit_release(%Qubit* %outputQubit)
  %18 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 0)
  %19 = bitcast i8* %18 to %Qubit**
  %20 = load %Qubit*, %Qubit** %19, align 8
  call fastcc void @Microsoft__Quantum__Intrinsic__H__body(%Qubit* %20)
  %21 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 0)
  %22 = bitcast i8* %21 to %Qubit**
  %23 = load %Qubit*, %Qubit** %22, align 8
  call fastcc void @Microsoft__Quantum__Intrinsic__X__body(%Qubit* %23)
  %24 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 1)
  %25 = bitcast i8* %24 to %Qubit**
  %26 = load %Qubit*, %Qubit** %25, align 8
  call fastcc void @Microsoft__Quantum__Intrinsic__Z__body(%Qubit* %26)
  %27 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 0)
  %28 = bitcast i8* %27 to %Qubit**
  %29 = load %Qubit*, %Qubit** %28, align 8
  %30 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 1)
  %31 = bitcast i8* %30 to %Qubit**
  %32 = load %Qubit*, %Qubit** %31, align 8
  call fastcc void @Microsoft__Quantum__Intrinsic__CNOT__body(%Qubit* %29, %Qubit* %32)
  %33 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 1)
  %34 = bitcast i8* %33 to %Qubit**
  %35 = load %Qubit*, %Qubit** %34, align 8
  call fastcc void @Microsoft__Quantum__Intrinsic__Z__adj(%Qubit* %35)
  %36 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 0)
  %37 = bitcast i8* %36 to %Qubit**
  %38 = load %Qubit*, %Qubit** %37, align 8
  call fastcc void @Microsoft__Quantum__Intrinsic__X__adj(%Qubit* %38)
  %39 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 0)
  %40 = bitcast i8* %39 to %Qubit**
  %41 = load %Qubit*, %Qubit** %40, align 8
  call fastcc void @Microsoft__Quantum__Intrinsic__H__adj(%Qubit* %41)
  %42 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 0)
  %43 = bitcast i8* %42 to %Qubit**
  %qubit = load %Qubit*, %Qubit** %43, align 8
  %r0 = call %Result* @__quantum__qis__m__body(%Qubit* %qubit)
  %44 = call i8* @__quantum__rt__array_get_element_ptr_1d(%Array* %qubits, i64 1)
  %45 = bitcast i8* %44 to %Qubit**
  %qubit__1 = load %Qubit*, %Qubit** %45, align 8
  %r1 = call %Result* @__quantum__qis__m__body(%Qubit* %qubit__1)
  call void @__quantum__rt__array_update_alias_count(%Array* %qubits, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %r0, i32 -1)
  call void @__quantum__rt__result_update_reference_count(%Result* %r1, i32 -1)
  call void @__quantum__rt__qubit_release_array(%Array* %qubits)
  ret void
}

declare %Qubit* @__quantum__rt__qubit_allocate() local_unnamed_addr

declare %Array* @__quantum__rt__qubit_allocate_array(i64) local_unnamed_addr

declare void @__quantum__rt__qubit_release_array(%Array*) local_unnamed_addr

declare void @__quantum__rt__array_update_alias_count(%Array*, i32) local_unnamed_addr

declare i8* @__quantum__rt__array_get_element_ptr_1d(%Array*, i64) local_unnamed_addr

declare void @__quantum__rt__qubit_release(%Qubit*) local_unnamed_addr

define internal fastcc void @Microsoft__Quantum__Intrinsic__X__body(%Qubit* %qubit) unnamed_addr {
entry:
  call void @__quantum__qis__x__body(%Qubit* %qubit)
  ret void
}

define internal fastcc void @Microsoft__Quantum__Intrinsic__X__adj(%Qubit* %qubit) unnamed_addr {
entry:
  call fastcc void @Microsoft__Quantum__Intrinsic__X__body(%Qubit* %qubit)
  ret void
}

define internal fastcc void @Microsoft__Quantum__Intrinsic__Z__body(%Qubit* %qubit) unnamed_addr {
entry:
  call void @__quantum__qis__z__body(%Qubit* %qubit)
  ret void
}

define internal fastcc void @Microsoft__Quantum__Intrinsic__Z__adj(%Qubit* %qubit) unnamed_addr {
entry:
  call fastcc void @Microsoft__Quantum__Intrinsic__Z__body(%Qubit* %qubit)
  ret void
}

declare %Result* @__quantum__qis__m__body(%Qubit*) local_unnamed_addr

declare void @__quantum__rt__result_update_reference_count(%Result*, i32) local_unnamed_addr

declare void @__quantum__qis__cnot__body(%Qubit*, %Qubit*) local_unnamed_addr

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__x__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__z__body(%Qubit*) local_unnamed_addr

declare %String* @__quantum__rt__string_create(i8*) local_unnamed_addr

declare void @__quantum__qis__t__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__t__adj(%Qubit*) local_unnamed_addr

define void @Microsoft__Quantum__Samples__SimpleGrover__SearchForMarkedInput__Interop() local_unnamed_addr #0 {
entry:
  call fastcc void @Microsoft__Quantum__Samples__SimpleGrover__SearchForMarkedInput__body()
  ret void
}

define void @Microsoft__Quantum__Samples__SimpleGrover__SearchForMarkedInput() local_unnamed_addr #1 {
entry:
  call fastcc void @Microsoft__Quantum__Samples__SimpleGrover__SearchForMarkedInput__body()
  %0 = call %String* @__quantum__rt__string_create(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @0, i64 0, i64 0))
  call void @__quantum__rt__message(%String* %0)
  call void @__quantum__rt__string_update_reference_count(%String* %0, i32 -1)
  ret void
}

declare void @__quantum__rt__message(%String*) local_unnamed_addr

declare void @__quantum__rt__string_update_reference_count(%String*, i32) local_unnamed_addr

attributes #0 = { "InteropFriendly" }
attributes #1 = { "EntryPoint" }
